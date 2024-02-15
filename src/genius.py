# Genius
# https://open.kattis.com/problems/genius
# TAGS: mathematics, probability, dynamic programming, nice
# CP4: 5.5b, Probability, Harder
# NOTES:
"""
Nice exercise.

Below, I left the recursive logic (which times out TLE for me in Python) which I used to gain
practice and understanding how to move from the recursive to the bottom-up dp approach.

---

from functools import lru_cache

def dp(preds, i, corrects):
    @lru_cache
    def helper(i, corrects):
        if corrects >= k: # RETURN EARLY
            return 1
        elif i >= len(preds):
            return 0

        prob_this = preds[i] * dp(preds, i + 1, corrects + 1)
        prob_not_this = (1 - preds[i]) * dp(preds, i + 1, corrects)

        return prob_this + prob_not_this
    return helper(i, corrects)

res = dp(winners_probs_given_predictions, 0, 0)

print(res)
"""
k, t, p, q, x = map(int, input().split())

#1) winner prediction part
predictions = [x % 4]
for _ in range(t - 1):
    x = (x * p) % q
    predictions.append(x % 4)

#2) tournament part - what is the probability that predictions' player i wins tournament i
tournaments = []
for _ in range(t):
    l = input()
    tournaments.append(list(map(int, l.split())))

#2) continued: probability that prediction i wins tournament i
tournaments_win_prob_breakdowns = []
for tournament in tournaments:
    p0, p1, p2, p3 = tournament # players and their strategy weights
    first_round = [p0 / (p0 + p1), p1 / (p0 + p1), p2 / (p2 + p3), p3 / (p2 + p3)] # win probs first round
    final_round = [first_round[0] * p0 * (first_round[2] / (p0 + p2) + first_round[3] / (p0 + p3)),  first_round[1] * p1 * (first_round[2] / (p1 + p2) + first_round[3] / (p1 + p3)), first_round[2] * p2 * (first_round[0] / (p2 + p0) + first_round[1] / (p2 + p1)), first_round[3] * p3 * (first_round[0] / (p3 + p0) + first_round[1] / (p3 + p1))]
    tournaments_win_prob_breakdowns.append(final_round)

winners_probs_given_predictions = [tournaments_win_prob_breakdowns[i][p] for i, p in enumerate(predictions)]

# After solving via recursion (and get TLE): derive the bottom-up dp approach
# Track the probability flow into the different dp states
# Rows are number of tournaments processed (0, 1, 2, ...t)
# Cols are number of correct predictions (0, 1, 2, ...t)
# dp state dp[t_][k_] is prob to have exactly k_ correct predictions having processed the first t_ tournaments
# INITIAL CONDITION IS dp[0][0] = 1, all the probability is in this initial state
# As we increase "rows" i.e. process more tournaments, we obtain non-zero probability in states corresponding to 1, then 2, then 3 correct predictions i.e. columns 1,2,3..
# THE RESULT IS ADDITIVE PROBABILITY IN THE FINAL, t'th, ROW - ALL THE STATES WHICH HAVE k_ >= k (where k is from statement; i.e. the min number of correct predictions needed to win the Genius game etc.)
dp = [[0] * (t + 1) for _ in range(t + 1)]
dp[0][0] = 1 # the probability of having exactly 0 correct guesses after processing exactly 0 tournaments is == 1

# bottom up implementation of the same recursive logic (see code in Notes)
for num_tournaments, guess_win_prob in enumerate(winners_probs_given_predictions, 1): # <-- enumerate from 1 since row 0 is the initial condition of having processed 0 tournaments
    for corrects in range(t):
        previous_dp_state = dp[num_tournaments - 1][corrects]
        dp[num_tournaments][corrects + 1] += guess_win_prob * previous_dp_state # if our prediction for this tournament is correct, propagate from previous state with -1 tournaments and now have +1 correct guesses
        dp[num_tournaments][corrects] += (1 - guess_win_prob) * previous_dp_state  # if our prediction for this tournament is incorrect, propagate from previous state with -1 tournaments WITH PROB (1-p)  and with same number of correct guesses

# the total prob that we made at least k correct predictions after a total of t tournaments is the sum of the probability in the t'th row of the dp board at columns >= k
# mini optimization to perform fewer additions: if k < t//2, sum the "bad probability" and take 1 - sum for the "good probability"
if k >= t // 2:
    res = sum(dp[t][k_] for k_ in range(k, t + 1))
else:
    res = 1 - sum(dp[t][_k] for _k in range(k))

print(res)