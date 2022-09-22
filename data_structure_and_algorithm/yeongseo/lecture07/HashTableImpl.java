package lecture07;

// insert, delete , search

import java.util.ArrayList;
import java.util.Objects;

class KeyValueEntry<k, v> {
    k key;
    v value;
    final int hashCode;
    KeyValueEntry<k, v> next;

    public KeyValueEntry(k key, v value, int hashCode) {
        this.key = key;
        this.value = value;
        this.hashCode = hashCode;
    }
}

public class HashTableImpl<k, v> {
    // 테이블이 될 ArrayList
    private ArrayList<KeyValueEntry> table;

    // 버킷의 최대 갯수(ArrayList의 크기)
    private int capacity;

    // 버킷의 현재 갯수
    private int size;

    public HashTableImpl() {
        this.table = new ArrayList<>();
        this.capacity = 5;
        this.size = 0;

        // 최대갯수만큼 null값 -> 링크드리스트 만들 것
        for (int i = 0; i < capacity; i++) {
            table.add(null);
        }
    }

    public int size() {
        return size;
    }

    private int getBucketIndex(k key) { // 나머지 연산법 사용

        // key -> hashCode -> hash modulo로 index

        int hashCode = hashCode(key);

        int index = hashCode % capacity;

        return index;
    }

    private final int hashCode(k key) {
        return Objects.hashCode(key);
    }

    public void add(k key, v value) {
        int BucketIndex = getBucketIndex(key);
        int hashCode = hashCode(key);
        System.out.println("key : " + key + ", hashCode : " + hashCode);

        KeyValueEntry<k, v> entry = table.get(BucketIndex);

        // 키가 이미 있다면, 키의 값을 바꿈
        while (entry != null) {
            if (entry.key.equals(key) && hashCode == entry.hashCode) {
                entry.value = value;
                return;
            }
            entry = entry.next;
        }

        // 키가 없는 경우 chain의 처음에 엔트리 추가
        size++;
        KeyValueEntry head = table.get(BucketIndex);
        KeyValueEntry<k, v> newNode = new KeyValueEntry<k, v>(key, value, hashCode);
        newNode.next = head;
        table.set(BucketIndex, newNode);

        // load factor 0.7 넘으면 크기 두배로
        // 확장(https://docs.oracle.com/javase/8/docs/api/java/util/Hashtable.html 에 따라)
        if ((1.0 * size) / capacity >= 0.7) {
            // 기존 테이블은 temp에 저장해두고
            ArrayList<KeyValueEntry> temp = table;

            // 새로운 테이블 생성
            table = new ArrayList<>();

            // capacity 두배로
            capacity = 2 * capacity;
            size = 0;

            // capacity만큼 테이블 확장하고
            for (int i = 0; i < capacity; i++)
                table.add(null);

            // 기존 테이블의 값들 다시 add해줌
            System.out.println("add again!");
            System.out.println("size : " + size);
            System.out.println("capacity : " + capacity);
            for (KeyValueEntry<k, v> headNode : temp) {
                while (headNode != null) {
                    add(headNode.key, headNode.value);
                    headNode = headNode.next;
                }
            }
        }
    }

    public v get(k key) {
        // 주어진 키의 테이블인덱스(bucketIndex), 키값의 hashCode 찾음
        int bucketIndex = getBucketIndex(key);
        int hashCode = key.hashCode();

        KeyValueEntry<k, v> head = table.get(bucketIndex);

        // 체인에서 키를 찾아서 값 리턴
        while (head != null) {
            if (head.key.equals(key) && head.hashCode == hashCode)
                return head.value;
            head = head.next;
        }

        // 만약 키가 없다면
        return null;
    }

    public v remove(k key) {
        // 키의 테이블 인덱스와, 그것의 해시코드 찾음
        int index = getBucketIndex(key);
        int hashCode = hashCode(key);

        // 테이블 인덱스 통해 체인의 헤드 찾음

        KeyValueEntry<k, v> head = table.get(index);

        // 체인에서 키 찾음(해시코드 사용)
        KeyValueEntry<k, v> prev = null;
        while (head != null) {
            if (head.key == key && head.hashCode == hashCode) {
                break;
            }
            prev = head;
            head = head.next;
        }

        // 만약 찾지 못했다면
        if (head == null) {
            return null;
        }

        // 사이즈 줄임
        size--;

        // 키를 삭제
        if (prev != null) {
            prev.next = head.next;
        } else { // head가 맨 앞인 경우
            table.set(index, head.next);
        }

        return head.value;
    }

    public static void main(String[] args) {
        HashTableImpl<String, Integer> table = new HashTableImpl<>();
        table.add("this", 1);
        table.add("coder", 2);
        table.add("third", 3);
        table.remove("third");
        System.out.println(table.get("coder"));
        System.out.println(table.size());
        System.out.println(table.capacity);
        table.add("this", 4);
        table.add("hi", 5);
        table.add("seven", 7);
        table.add("six", 6);
        table.add("eight", 8);
        table.add("57", 8);

        System.out.println(table.size());
        System.out.println(table.capacity);

        System.out.println("여기부터");
        System.out.println(table.table.get(0));
        System.out.println(table.table.get(1));
        System.out.println(table.table.get(2));
        System.out.println(table.table.get(3));
        System.out.println(table.table.get(4));
        System.out.println(table.table.get(5));
        System.out.println(table.table.get(6));
        System.out.println(table.table.get(7));
        System.out.println(table.table.get(8));
        System.out.println(table.table.get(9));
        System.out.println(table.table.get(10));
        System.out.println(table.table.get(11));
        System.out.println(table.table.get(12));
        System.out.println(table.table.get(13));
        System.out.println(table.table.get(14));
        System.out.println(table.table.get(15));
    }
}
