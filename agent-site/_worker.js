const LINK_HEADER = [
  '</.well-known/agent-skills/index.json>; rel="service-desc"; type="application/json"',
  '</llms.txt>; rel="describedby"; type="text/plain"',
].join(', ');

function responseWithHeaders(response, { home = false } = {}) {
  const headers = new Headers(response.headers);
  headers.set('Access-Control-Allow-Origin', '*');
  headers.set('X-Content-Type-Options', 'nosniff');
  if (home) headers.set('Link', LINK_HEADER);
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers,
  });
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const wantsMarkdown = (request.headers.get('Accept') || '')
      .toLowerCase()
      .includes('text/markdown');

    if (url.pathname === '/' && wantsMarkdown) {
      const markdownUrl = new URL('/index.md', url);
      const markdown = await env.ASSETS.fetch(new Request(markdownUrl, request));
      const headers = new Headers(markdown.headers);
      headers.set('Content-Type', 'text/markdown; charset=utf-8');
      headers.set('Vary', 'Accept');
      headers.set('Link', LINK_HEADER);
      headers.set('Access-Control-Allow-Origin', '*');
      headers.set('X-Content-Type-Options', 'nosniff');
      return new Response(markdown.body, {
        status: markdown.status,
        statusText: markdown.statusText,
        headers,
      });
    }

    return responseWithHeaders(await env.ASSETS.fetch(request), {
      home: url.pathname === '/',
    });
  },
};
