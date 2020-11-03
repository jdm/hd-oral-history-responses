let chars = ['-', '_'];
for (let c = 0; c < 26; c++) {
    chars.push(String.fromCharCode(c + 'a'.charCodeAt(0)));
}
for (let c = 0; c < 10; c++) {
    chars.push(String.fromCharCode(c + '0'.charCodeAt(0)));
}

function createTrieFor(origNames, root, prefix) {
    let names = [...origNames];

    // FIXME: only use the first character of actual names present
    for (let c of chars) {
        // Get all words that start with the given letter.
        let matching = names.filter((n) => n.startsWith(prefix + c));
        if (matching.length === 0) {
            continue;
        }
        // Remove from the original list.
        for (const name of matching) {
            names.splice(names.indexOf(name), 1);
        }
        if (matching.length == 1 && prefix.length > 0) {
            root.set(matching[0].slice(prefix.length), matching[0]);
        } else {
            let newRoot = new Map();
            root.set(c, newRoot);
            createTrieFor(matching, newRoot, prefix + c)
        }
    }

    if (names.length) {
        console.error(names, prefix);
    }
}

function completeMatching(search, prefix, root) {
    if (search.length) {
        let branch = root.get(search[0]);
        if (branch !== undefined) {
            return completeMatching(search.slice(1), prefix + search[0], branch);
        }
        let results = [];
        for (const [key, value] of root) {
            if (key.startsWith(search)) {
                results.push(value);
            }
        }
        return results;
    }

    let results = [];
    let stack = [root];
    while (stack.length) {
        let node = stack.pop();
        for (const value of node.values()) {
            if (value instanceof Map) {
                stack.push(value);
            } else {
                results.push(value);
            }
        }
    }
    return results;
}
