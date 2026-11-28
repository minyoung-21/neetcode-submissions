class Solution {
    public int leastInterval(char[] tasks, int n) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        int[] count = new int[26];
        Queue<int[]> q = new LinkedList<>();

        int res = 0;
        int time = 0;

        for (char t : tasks) {
            count[t-'A']++;
        }

        // added chars to maxHeap sorted
        
        for (int c : count) {
            if (c > 0) {
                maxHeap.add(c);
            }
        }

        // loop until heap gets empty or q gets empty

        while (!maxHeap.isEmpty() || !q.isEmpty()) {
            time += 1;

            if (maxHeap.isEmpty()) {
                time = q.peek()[1];
            } else {
                int c = maxHeap.poll() - 1;
                if (c > 0) {
                    q.add(new int[] {c, time+n});
                }
            }

            if (!q.isEmpty() && q.peek()[1] == time) {
                maxHeap.add(q.poll()[0]);
            }
        }

        return time;
    }
}
