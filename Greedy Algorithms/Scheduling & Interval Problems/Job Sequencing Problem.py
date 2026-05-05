class Solution:
    def JobScheduling(self, jobs):
        # your code goes here
        """
        T.C. : O(nlogn) for sorting the jobs array + O(n*maxDeadline) for iterating through the jobs array and the hash array where maxDeadline is the maximum deadline among the jobs
        S.C. : O(maxDeadline) for the hash array to store the job ids for each deadline where maxDeadline is the maximum deadline among the jobs
        """
        jobs.sort(key=lambda x: -x[2])
        n = len(jobs)
        maxDeadLine = -1

        for i in jobs:
            maxDeadLine = max(maxDeadLine, i[1])

        hash = [-1]*maxDeadLine
        cnt, ans = 0, 0

        for i in range(n):
            for j in range(jobs[i][1]-1, -1, -1):
                if hash[j] == -1:
                    cnt += 1
                    hash[j] = jobs[i][0]
                    ans += jobs[i][2]
                    break
        return [cnt, ans]
