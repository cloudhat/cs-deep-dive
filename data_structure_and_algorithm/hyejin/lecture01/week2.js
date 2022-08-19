// 재귀 연습

// 기저 조건 : 우주선 카운트다운 함수 만들기
    
// 1. 기저 조건 (base case) 
// - 함수가 반복되지 않는 경우. 아래 함수에서는 0이 기저 조건이다
// - 모든 재귀 함수는 무한대로 호출되지 않게 하는 기저 조건이 적어도 하나 있어야 한다

    // Loop
    function countdown(number) {
        for(let i = number; i >= 0, i--) {
            console.log(i);
        }
    }
    countdown(10);

    // Recursive
    function countdown(number) {
        if (number < 0) return;
        console.log(number);
        countdown(number - 1);
    }
    
// 2. 계승 (factorial)
function factorial(number) {
    if (number === 1) return;
    return number * factorial(number - 1);
}

/* 연습 1 
    low부터 high까지의 수를 하나 걸러 하나씩 출력한다.
    에를 들어 low가 0이고, high가 10이면 다음과 같이 출력한다
    다음 함수의 기저 조건을 알아내자 

    0
    2
    4
    6
    8
    10
*/

function print_every_other(low, high) {
    if (low > high) return;
    console.log(low);
    print_every_otehr(low + 2, high);
}

// 기저 조건 : low < high

/* 연습 2
    다음 함수는 low부터 high까지 모든 수의 합을 반환한다.
    예를 들어 low 1, high 10이면 1부터 10까지의 합인 55를 반환한다.
    올바른 기저 조건을 넣어 코드를 수정하자.
*/

function sum(low, high) {
    if (low === high) return low; // base case
    return high + sum(low, high - 1); 
}

/* 연습 3
    배열 내 모든 숫자를 출력하는 재귀 함수를 작성하라.
    array= [1, 2, 3, [4,5,6], 7, [8, [9, 10, 11, [12, 13, 14]]], [15, 16, 17, 18, 19, [20, 21, 22, [23, 24, 25, [26, 27, 29], 30, 31], 32], 33]]
*/

function print_array_number(array) {
    for (value of array) {
        // value가 배열인지 판단
        if(Array.isArray(value)) print_array_number(value);
        // 기저 조건 - 배열이 아니면 출력 한다
        console.log(value);
    }
}
    
    