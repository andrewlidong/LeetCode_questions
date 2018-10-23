// Given a 2D board and a word, find if the word exists in the grid.
//
// The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
//
// Example:
//
let board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
];
//
// Given word = "ABCCED", return true.
// Given word = "SEE", return true.
// Given word = "ABCB", return false.

/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    for (let i = 0; i < board.length; i++) {
        for (let j = 0; j < board[0].length; j++) {
            if (board[i][j] === word[0]) {
                let nextSearch = searcher(board, i, j, word, 0);
                if (nextSearch) {
                    return true;
                }
            }
        }
    }
    return false;
};

let searcher = function(board, i, j, word, wordCount) {
    if (i < 0 || i >= board.length || j < 0 || j >= board[i].length || board[i][j] !== word[wordCount]) {
        return false;
    }
    board[i][j] = "-";
    if (wordCount === word.length - 1) {
        return true;
    }

    let count = wordCount + 1;
      if(searcher(board,i+1,j,word,count) || searcher(board,i-1,j,word,count) || searcher(board,i,j+1,word,count) || searcher(board,i,j-1,word,count)) {
        return true;
    } else {
        board[i][j] = word[wordCount];
        return false;
    }
};


// STUDENT SOLUTION
// function wordAtPoint(grid, point, word) {
//     const dirs = [[1,0], [-1,0], [0,1], [0,-1]];
//     let char_idx = 0;
//     let location = [point[0], point[1]]
//     for (dir of dirs) {
//         if (location[0] + dir[0] < 0 || location[0] + dir[0] >== grid.length) {
//             next;
//         }
//         while (grid[location[0]][location[1]] === word[char_idx]) {
//             location[0] += dir[0];
//             location[1] += dir[1];
//             char_idx += 1;
//         }
//         if (char_idx === word.length - 1) {
//             return true;
//         } else {
//             location = [point[0], point[1]];
//             char_idx = 0;
//         }
//         return false;
//     }
// }
