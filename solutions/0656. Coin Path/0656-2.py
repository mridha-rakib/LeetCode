class Solution:
  def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
    if coins[-1] == -1:
      return []

    n = len(coins)
    # dp[i] := min cost to jump to n - 1 from i
    dp = [math.inf] * n
    next = [-1] * n

    dp[-1] = coins[-1]

    for i in reversed(range(n - 1)):
      if coins[i] == -1:
        continue
      for j in range(i + 1, min(i + maxJump + 1, n)):
        if dp[j] == math.inf:
          continue
        cost = coins[i] + dp[j]
        if cost < dp[i]:
          dp[i] = cost
          next[i] = j

    if dp[0] == math.inf:
      return []
    return self._constructPath(next, 0)

  def _constructPath(self, next: List[int], i: int) -> List[int]:
    ans = []
    while i != -1:
      ans.append(i + 1)  # 1-indexed
      i = next[i]
    return ans
