"use strict";
const graph = JSON.parse(document.querySelector("#diagram-data").textContent);
const levels = JSON.parse(document.querySelector("#diagram-order").textContent);
const rank = new Map(levels.map(([name], i) => ["otype::" + name, i]));
const svg = document.querySelector("#diagram");
const select = document.querySelector("#diagram-focus");
const reference = document.querySelector("#diagram-reference");
const svgNS = "http://www.w3.org/2000/svg";

function element(tag, attrs, parent) {
  const child = document.createElementNS(svgNS, tag);
  for (const [key, value] of Object.entries(attrs)) child.setAttribute(key, value);
  parent.append(child);
  return child;
}

function label(id) {
  return graph.nodes[id].origName || graph.nodes[id].featureName;
}

function url(id) {
  const name = encodeURIComponent(label(id));
  return rank.has(id) ? "structure.html#type-" + name : "features/" + name + ".html";
}

// Use one vote per populated type. Large populations of slots would otherwise
// pull shared features to the bottom even when they annotate broad types too.
function center(id) {
  const types = graph.nodes[id].valid_on;
  if (!types.length) return levels.length;
  return types.reduce((total, type) => total + rank.get(type), 0) / types.length;
}

function render() {
  const focus = select.value;
  const edges = graph.edges.filter(edge => !focus || edge.from === focus || edge.to === focus);
  const visible = focus ? new Set([focus, ...edges.flatMap(e => [e.from, e.to])]) : new Set(Object.keys(graph.nodes));
  const features = [...visible].filter(id => !rank.has(id));
  features.sort((a, b) => center(a) - center(b) || label(a).localeCompare(label(b), "en"));
  const groups = Array.from({length: levels.length + 1}, () => []);
  for (const feature of features) groups[Math.round(center(feature))].push(feature);

  const positions = new Map();
  let y = 44;
  for (const [i, group] of groups.entries()) {
    const type = i < levels.length ? "otype::" + levels[i][0] : null;
    if (!visible.has(type) && !group.length) continue;
    const rows = Math.max(1, Math.ceil(group.length / 2));
    if (visible.has(type)) positions.set(type, [480, y + (rows - 1) * 19]);
    group.forEach((id, j) => positions.set(id, [j % 2 ? 816 : 144, y + Math.floor(j / 2) * 38]));
    y += rows * 38 + 14;
  }

  svg.replaceChildren();
  svg.setAttribute("viewBox", "0 0 960 " + y);
  for (const [x, title] of [[144,"Features"], [480,"Node types"], [816,"Features"]]) {
    element("text", {x, y:17, class:"column-label"}, svg).textContent = title;
  }
  for (const edge of edges) {
    const [x1,y1] = positions.get(edge.from);
    const [x2,y2] = positions.get(edge.to);
    const direction = Math.sign(x2 - x1);
    const start = x1 + direction * 124;
    const end = x2 - direction * 100;
    const mid = (start + end) / 2;
    const path = element("path", {d:"M " + start + " " + y1 + " C " + mid + " " + y1 + ", " + mid + " " + y2 + ", " + end + " " + y2}, svg);
    element("title", {}, path).textContent = label(edge.from) + " applies to " + label(edge.to);
  }
  for (const [id,[x,y]] of positions) {
    const isType = rank.has(id);
    const width = isType ? 200 : 248;
    const a = element("a", {href:url(id), class:(isType ? "type" : "feature") + (id === focus ? " selected" : "")}, svg);
    const name = label(id);
    const tip = isType ? levels[rank.get(id)][1].toLocaleString(undefined,{maximumFractionDigits:2}) + " slots per node on average" : graph.nodes[id].description;
    element("title", {}, a).textContent = name + (tip ? " · " + tip : "");
    element("rect", {x:x-width/2,y:y-14,width,height:28,rx:isType ? 14 : 4}, a);
    const text = element("text", {x,y:y+5}, a);
    text.textContent = name;
    if (text.getComputedTextLength() > width - 18) {
      text.setAttribute("textLength", width - 18);
      text.setAttribute("lengthAdjust", "spacingAndGlyphs");
    }
    a.addEventListener("click", event => {
      if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      select.value = id;
      render();
      select.focus({preventScroll:true});
    });
  }
  reference.hidden = !focus;
  if (focus) reference.href = url(focus);
  document.querySelector("#diagram-status").textContent =
    (focus ? label(focus) + " · " : "") + visible.size + " nodes · " + edges.length + " connections. Select a node to explore its neighbors.";
}
select.addEventListener("change", render);
document.querySelector("#diagram-reset").addEventListener("click", () => { select.value = ""; render(); });
render();
