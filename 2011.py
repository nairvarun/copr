class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        return sum(list(map(lambda x: int(x), (list(map(lambda x: x.replace('++X', '1').replace('X++', '1').replace('--X', '-1').replace('X--', '-1'), operations))))))

operations = ["--X","X++","X++"]
print(Solution.finalValueAfterOperations(Solution, operations))
