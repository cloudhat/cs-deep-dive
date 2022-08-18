// 1.2-2
// 삽입 정렬이 병합 정렬을 능가하는 n 값은 무엇입니까? (삽입정렬 값 > 병합정렬 값)

let i = 2;

while (8 * i ** 2 < 64 * i * Math.sqrt(i)) {
  i++;
}

console.log(i + 1); // 65

// 1.2-3
// 100n제곱이 2n승보다 빠르게 실행되는 n의 최소값은 무엇입니까? (100n제곱 값 < 2n승 값)

let n = 2;

while (100 * n ** 2 > Math.pow(2, n)) {
  n++;
}

console.log(n); // 15
