import java.util.ArrayList;

public class countingSort {
    static ArrayList<Integer> sort(int[] arr, int k) {
        int n = arr.length;

        int[] Llist = new int[k+1];

        for (int i : arr) { // O(n)
            Llist[i] += 1; // 인덱스에 해당하는 값의 개수를 기록
        }

        ArrayList<Integer> result = new ArrayList<>();

        for (int i =1; i<Llist.length; i++) { // O(k*n)
            if (Llist[i] != 0) {
                for (int j=0; j<Llist[i]; j++) {
                    result.add(i);
                }
            }
        }

        return result;
    }

    static ArrayList<Integer> AdvancedSort(int[] arr, int k) { //O(n+k)

        ArrayList[] Llist = new ArrayList[k+1];

        for (int i=1; i<k+1; i++) { // 2차원 ArrayList
            Llist[i] = new ArrayList<Integer>();
        }

        for (int i: arr) {  // O(n)
            Llist[i].add(i); // 인덱스에 해당하는 값의 개수만큼 어레이리스트 만듬
        }

        ArrayList result = new ArrayList<>();

        for (int i = 0 ; i< k+1; i++) { // O(k)
            if (Llist[i] != null) {
                result.addAll(Llist[i]);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] arr = {2,1,1,1,5,5,3,7,6,9,8,2,10};

        ArrayList result = sort(arr, 10);
        System.out.println(result);

        ArrayList result2 = AdvancedSort(arr, 10);
        System.out.println(result2);
    }
}
