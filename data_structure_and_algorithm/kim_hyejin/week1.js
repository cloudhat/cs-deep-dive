// 1.2-2
// 삽입 정렬이 병합 정렬을 능가하는 n 값은 무엇입니까? (삽입 정렬이 더 빠를 때의 n값)

for (let n = 2; 8 * n ** 2 < 64 * n * Math.sqrt(n); n++) {
  console.log("beat value", n);
}

// 1.2-3
// 100n제곱이 2n승보다 빠르게 실행되는 n의 최소값은 무엇입니까?

for (let n = 2; 100 * n ** 2 > Math.pow(n, 2); n++) {
  console.log("beat value", n);
}
