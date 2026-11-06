const filter = document.querySelector("#filter");
filter?.addEventListener("input", () => {
  const query = filter.value.trim().toLowerCase();
  for (const row of document.querySelectorAll("tbody tr")) {
    row.hidden = !row.textContent.toLowerCase().includes(query);
  }
});
function revealType() {
  const target = document.getElementById(decodeURIComponent(location.hash.slice(1)));
  if (target instanceof HTMLDetailsElement) target.open = true;
}
window.addEventListener("hashchange", revealType);
revealType();
const focusNode = document.querySelector("#focus");
if (focusNode) {
  const graph = JSON.parse(document.querySelector("#graph").textContent);
  const panel = document.querySelector("#neighbors");
  function draw() {
    const id = focusNode.value;
    const record = graph.nodes[id];
    const heading = document.createElement("h3");
    heading.textContent = record.featureName || record.origName;
    const links = document.createElement("div");
    links.className = "neighbors";
    for (const edge of graph.edges) {
      if (edge.from !== id && edge.to !== id) continue;
      const target = edge.from === id ? edge.to : edge.from;
      const button = document.createElement("button");
      button.textContent = target.split("::")[1];
      button.addEventListener("click", () => { focusNode.value = target; draw(); });
      links.append(button);
    }
    const label = document.createElement("p");
    label.textContent = record.featureName ? "Applies to these node types" : "Features populated on this node type";
    const detail = document.createElement("a");
    detail.href = record.featureName ? "features/" + encodeURIComponent(record.featureName) + ".html" : "#type-" + encodeURIComponent(record.origName);
    detail.textContent = "Open reference";
    panel.replaceChildren(heading, detail, label, links);
  }
  focusNode.addEventListener("change", draw);
  draw();
}
