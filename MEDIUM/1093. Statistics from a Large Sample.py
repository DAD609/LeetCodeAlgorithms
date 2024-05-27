'''
You are given a large sample of integers in the range [0, 255]. Since the sample is so large, it is represented by an array count where count[k] is the number of times that k appears in the sample.

Calculate the following statistics:

minimum: The minimum element in the sample.
maximum: The maximum element in the sample.
mean: The average of the sample, calculated as the total sum of all elements divided by the total number of elements.
median:
If the sample has an odd number of elements, then the median is the middle element once the sample is sorted.
If the sample has an even number of elements, then the median is the average of the two middle elements once the sample is sorted.
mode: The number that appears the most in the sample. It is guaranteed to be unique.
Return the statistics of the sample as an array of floating-point numbers [minimum, maximum, mean, median, mode]. Answers within 10-5 of the actual answer will be accepted.
'''

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
       
        total_sum = 0
        total_count = 0
        minimum = None
        maximum = None
        mode = None
        mode_count = 0
      
        for i in range(256):
            if count[i] > 0:
                if minimum is None:
                    minimum = i
                maximum = i
                total_sum += i * count[i]
                total_count += count[i]
                if count[i] > mode_count:
                    mode_count = count[i]
                    mode = i
        mean = total_sum / total_count
        cumulative_count = 0
        median = 0
        if total_count % 2 == 1: 
            median_index = total_count // 2
            for i in range(256):
                cumulative_count += count[i]
                if cumulative_count > median_index:
                    median = i
                    break
        else: 
            median_index1 = total_count // 2 - 1
            median_index2 = total_count // 2
            first_median_value = None
            for i in range(256):
                cumulative_count += count[i]
                if cumulative_count > median_index1 and first_median_value is None:
                    first_median_value = i
                if cumulative_count > median_index2:
                    median = (first_median_value + i) / 2
                    break
        return [float(minimum), float(maximum), mean, median, float(mode)]
