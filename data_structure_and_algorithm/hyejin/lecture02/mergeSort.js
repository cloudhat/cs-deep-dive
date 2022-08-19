const merge = (array1, array2) => {
  let mergedList = [];
  let i = 0; // 왼쪽 배열의 index
  let j = 0; // 오른쪽 배열의 index

  // 비교 후 append
  while (i < array1.length && j < array2.length) {
    if (array1[i] > array2[j]) {
      mergedList = mergedList.concat(array2[j]);
      j += 1;
    } else {
      mergedList = mergedList.concat(array1[i]);
      i += 1;
    }
  }

  // 기저 조건 : append 이후 다 더했을 때
  if (i === array1.length) mergedList = mergedList.concat(array2.slice(j));
  if (j === array2.length) mergedList = mergedList.concat(array1.slice(i));

  return mergedList;
};

const mergeSort = (array) => {
  // 기저 조건 : 1개일 때
  if (array.length <= 1) return array;

  let mid = array.length / 2;

  const leftHalf = array.slice(0, mid);
  const rightHalf = array.slice(mid);

  return merge(mergeSort(leftHalf), mergeSort(rightHalf));
};

console.log(mergeSort([1, 3, 5, 7, 9, 11, 13, 11]));
console.log(mergeSort([28, 13, 9, 30, 1, 48, 5, 7, 15]));
