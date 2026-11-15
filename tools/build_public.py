#!/usr/bin/env python3
"""내 앱(trpg-wishlist.html) + 데이터(JSON) → 읽기 전용 공개 페이지.
사용: build_public.py <app.html> <wish.json> <played.json> <out.html>
wish.json: 위시 문서 목록(id 포함). played.json: [{"path"|"id", "data"{...}}] 또는 문서 목록."""
import json, sys, datetime
app, wishp, playedp, out = sys.argv[1:5]
s = open(app, encoding="utf-8").read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70]); s = s.replace(a, b)
wish = [x for x in json.load(open(wishp, encoding="utf-8")) if not x.get("deleted")]
for x in wish: x.pop("overview", None); x.pop("caution", None); x.pop("memo", None); x.pop("pending", None); x.pop("linkCheckedAt", None); x.pop("updatedAt", None)
played = []
for x in json.load(open(playedp, encoding="utf-8")):
    d = x.get("data", x)
    if d.get("deleted"): continue
    played.append({"id": x.get("path") or x.get("id"), "title": d["title"], "system": d.get("system") or "기타", "status": "done", "plays": d.get("plays", []), "createdAt": d.get("createdAt", 0)})
items = wish + played
rep('<title>TRPG 시나리오 위시리스트</title>', '<title>가고 싶은 TRPG 시나리오</title>')
rep('<body class="busy">', '<body class="ro">')
rep('  img.px{', '  body.ro #tbNew,body.ro #tbProp,body.ro #tbDel,body.ro #tbEmpty,body.ro .tsep,body.ro [data-act=new],body.ro [data-act=prop],body.ro [data-act=del],body.ro [data-act=export],body.ro [data-act=import],body.ro [data-edit],body.ro [data-open="smart:trash"],body.ro .menubar>span:nth-child(2),body.ro .startmenu hr:first-of-type{display:none!important}\n  img.px{')
rep('  function openForm(id){', '  function openForm(id){ return;')
rep('<div class="content" style="line-height:1.7;padding:12px 14px">',
    '<div class="content" style="line-height:1.7;padding:12px 14px"><b>가고 싶은 TRPG 시나리오</b><br>룰 폴더를 열면 가고 싶은 시나리오가 파일로 나옵니다. 파일을 누르면 인원·특징·태그·주의 키워드가 담긴 설명 창이 열리고, [열기]로 시나리오 페이지로 갈 수 있어요. 창은 여러 개 띄워 끌어 옮길 수 있습니다.<br><br>⭐ [당장 하고 싶은] 폴더에는 특히 가고 싶은 것만, ✔ [다녀온 시나리오] 폴더에는 이미 다녀온 시나리오가 룰별로 모여 있어요.<div hidden>')
rep('      <b>1:1 타이만</b><br>제목·태그 어디든 ‘타이만’이 있으면 1:1 시나리오로 분류됩니다.\n    </div>', '      </div>\n    </div>')
stamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y.%m.%d")
rep('  render(); init().finally(()=>document.body.classList.remove("busy"));',
    '  const DATA=' + json.dumps(items, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/") + ';\n  DATA.forEach(x=>items.set(x.id,x));\n  render(); note("읽기 전용 · ' + stamp + ' 기준");')
open(out, "w", encoding="utf-8").write(s)
print("built", out, "wish", len(wish), "played", len(played))
