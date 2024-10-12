class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []
        
        # Create events for each interval
        for start, end in intervals:
            events.append((start, 1))  # Start of an interval
            events.append((end + 1, -1))  # End of an interval (exclusive)

        # Sort events by time; if times are equal, prioritize end (-1) over start (+1)
        events.sort()

        max_overlap = 0
        current_overlap = 0

        # Traverse through sorted events
        for _, event_type in events:
            current_overlap += event_type
            max_overlap = max(max_overlap, current_overlap)

        return max_overlap

