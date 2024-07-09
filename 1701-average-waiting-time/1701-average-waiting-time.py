class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        A = len(customers)
        
        total_waiting_time = 0
        current_time = 0
        
        for arrival, preparation in customers:
            current_time = max(current_time, arrival)  # Chef starts at max of when chef is free and arrival time
            current_time += preparation  # Chef finishes preparing current order
            
            total_waiting_time += current_time - arrival  # Add waiting time for current customer
        
        return total_waiting_time / A
        