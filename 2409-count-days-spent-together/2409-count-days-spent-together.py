class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str,
                          arriveBob: str, leaveBob: str) -> int:

        alice_start = int(arriveAlice[:2]) * 100 + int(arriveAlice[3:])
        alice_end = int(leaveAlice[:2]) * 100 + int(leaveAlice[3:])
        bob_start = int(arriveBob[:2]) * 100 + int(arriveBob[3:])
        bob_end = int(leaveBob[:2]) * 100 + int(leaveBob[3:])

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)

        if start > end:
            return 0

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def day_of_year(date):
            month = date // 100
            day = date % 100
            return sum(days[:month - 1]) + day

        return day_of_year(end) - day_of_year(start) + 1
