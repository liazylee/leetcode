"""
<p>You are given an <code>n x n</code> integer matrix <code>board</code> where the cells are labeled from <code>1</code> to <code>n<sup>2</sup></code> in a <a href="https://en.wikipedia.org/wiki/Boustrophedon" target="_blank"><strong>Boustrophedon style</strong></a> starting from the bottom left of the board (i.e. <code>board[n - 1][0]</code>) and alternating direction each row.</p>

<p>You start on square <code>1</code> of the board. In each move, starting from square <code>curr</code>, do the following:</p>

<ul> 
 <li>Choose a destination square <code>next</code> with a label in the range <code>[curr + 1, min(curr + 6, n<sup>2</sup>)]</code>. </li>
</ul>

    <ul>
    	<li>This choice simulates the result of a standard <strong>6-sided die roll</strong>: i.e., there are always at most 6 destinations, regardless of the size of the board.</li>
    </ul>
    </li>
    <li>If <code>next</code> has a snake or ladder, you <strong>must</strong> move to the destination of that snake or ladder. Otherwise, you move to <code>next</code>.</li>
    <li>The game ends when you reach the square <code>n<sup>2</sup></code>.</li>


<p>A board square on row <code>r</code> and column <code>c</code> has a snake or ladder if <code>board[r][c] != -1</code>. The destination of that snake or ladder is <code>board[r][c]</code>. Squares <code>1</code> and <code>n<sup>2</sup></code> do not have a snake or ladder.</p>

<p>Note that you only take a snake or ladder at most once per move. If the destination to a snake or ladder is the start of another snake or ladder, you do <strong>not</strong> follow the subsequent&nbsp;snake or ladder.</p>

<ul> 
 <li>For example, suppose the board is <code>[[-1,4],[-1,3]]</code>, and on the first move, your destination square is <code>2</code>. You follow the ladder to square <code>3</code>, but do <strong>not</strong> follow the subsequent ladder to <code>4</code>.</li> 
</ul>

<p>Return <em>the least number of moves required to reach the square </em><code>n<sup>2</sup></code><em>. If it is not possible to reach the square, return </em><code>-1</code>.</p>

<p>&nbsp;</p> 
<p><strong class="example">Example 1:</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 500px; height: 394px;" /> 
<pre>
<strong>Input:</strong> board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre>
<strong>Input:</strong> board = [[-1,-1],[-1,3]]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p> 
<p><strong>Constraints:</strong></p>

<ul> 
 <li><code>n == board.length == board[i].length</code></li> 
 <li><code>2 &lt;= n &lt;= 20</code></li> 
 <li><code>board[i][j]</code> is either <code>-1</code> or in the range <code>[1, n<sup>2</sup>]</code>.</li> 
 <li>The squares labeled <code>1</code> and <code>n<sup>2</sup></code> do not have any ladders or snakes.</li> 
</ul>

<div><div>Related Topics</div><div><li>Array</li><li>Breadth-First Search</li><li>Matrix</li></div></div><br><div><li>👍 2741</li><li>👎 907</li></div>
"""
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get(s):
            quot,rem=divmod(s-1,n)
            row=n-1-quot
            col=rem if row%2!=n%2 else n-1-rem
            return row,col
        dist={1:0}
        queue=[1]
        while queue:
            s=queue.pop(0)
            if s==n*n:
                return dist[s]
            for s2 in range(s+1,min(s+6,n*n)+1):
                r,c=get(s2)
                if board[r][c]!=-1:
                    s2=board[r][c]
                if s2 not in dist:
                    dist[s2]=dist[s]+1
                    queue.append(s2)

        return -1
        
# leetcode submit region end(Prohibit modification and deletion)
