// On fait un parcours largeur simple

function treeByLevels (rootNode) {
  if (rootNode == null) {
    return [];
  }
  const res = [];
  let i = 0;
  const list = [];
  list.push(rootNode);
  list.push(true);
  while (i < list.length) {
    const curr = list[i];
    if (curr == true && i < list.length - 1 ) {
      list.push(true);
    }
    else {
      if (curr.left != null) {
        list.push(curr.left);
      }
      if (curr.right != null) {
        list.push(curr.right);
      }
    }
    i++;
  }
  for (let i = 0; i < list.length; i++) {
    if (list[i] != true) {
      res.push(list[i].value);
    }
  }
	return res;
}
