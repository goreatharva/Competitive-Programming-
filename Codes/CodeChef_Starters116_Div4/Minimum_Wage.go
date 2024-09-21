package main

import "fmt"

func main() {
    var X int
    fmt.Scanln(&X)

    if X > 11 {
        fmt.Println("YES")
    } else {
        fmt.Println("NO")
    }
}
