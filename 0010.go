package main

import "fmt"

func check_prime(num int) bool {
    var r int = num / 2
    for i := 3; i < r; i += 2 {
        if num % i == 0 {
            return false
        }
    }
    return true
}

func main() {
    var sum int = 2
    for i := 3; i < 2000000; i += 2 {
        if check_prime(i) {
            sum += i
        }
    }
    fmt.Print(sum, "\n")
}