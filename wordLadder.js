/**
 * @param {string} beginWord
 * @param {string} endWord
 * @param {string[]} wordList
 * @return {number}
 */
var ladderLength = function(beginWord, endWord, wordList) {
    var dict = new Set(wordList);
    if (beginWord == endWord) {
        return 1;
    }
    if (!dict.has(endWord)) {
        return 0;
    }
    return bfs(beginWord, endWord, dict);
};

var bfs = function(start, end, dict) {
    var q = [start];
    var count = 0, precount = 1, nextcount = 0;
    var level = 1;
    while(q.length > 0) {
        var cur = q.shift();
        count++;
        if (cur == end) {
            return level;
        }
        var curArr = cur.split("");
        for (var i = 0; i < curArr.length; ++i) {
            var prec = curArr[i];
            for (var j = 97; j <= 122; ++j) {
                var c = String.fromCharCode(j);
                if (c == prec) { continue; }
                curArr[i] = c;
                var w = curArr.join("");
                if (dict.has(w)) {
                    q.push(w);
                    nextcount++;
                    dict.delete(w);
                }
                curArr[i] = prec;
            }
        }
        if (q.length == 0) {
            break;
        }
        if (count == precount) {
            precount = nextcount;
            count = 0;
            nextcount = 0;
            level++;
        }
    }
    return 0;
};
