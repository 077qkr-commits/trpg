# 역설의 TRPG

윈도우 98 풍 TRPG 시나리오 위시리스트(읽기 전용 공개 페이지). https://077qkr-commits.github.io/trpg/

- `index.html` — 공개 페이지 (GitHub Pages로 서비스). 직접 고치지 말고 아래 명령으로 다시 만든다.
- `data/wish.json` — 위시 시나리오 목록 (문서 id 포함)
- `data/played.json` — 다녀온 시나리오 목록
- `tools/app.html`, `tools/build_public.py` — 공개 페이지를 다시 만드는 도구

다시 만들기: `python3 tools/build_public.py tools/app.html data/wish.json data/played.json index.html`
