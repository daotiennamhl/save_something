- COMBINATION OPERATOR:
    - withLastestFrom:
        + Gộp giá trị được emit từ Outer Observable với giá trị gần nhất của inner Observable
        + Phù hợp với nghiệp vụ mà cần lắng nghe Outer Observable và cần lấy thêm giá trị gần nhất của 1 Observable khác
    - combineLatest:
        + Mình chưa dùng bao giờ nhưng đọc khá nhiều về lý thuyết
        + combine state khi dùng Service trong Angular, thường kết hợp với async pipe để dùng trong template
    - forkJoin:
        + Chỉ emit khi tất cả các Observables thành phần complete, emit ra array của các giá trị cuối cùng mà mỗi observable thành phần emit
        + Giống Promise.all() khác ở chỗ là observable thì trả ra stream value và lấy phần tử cuối cùng của mỗi stream đó của observable
    - startWith:
        + Thường dùng để cung cấp giá trị ban đầu cho các API call
    - merge:
        + use case thường gặp là khi có 1 Formgroup và muốn lắng nghe vào từng FormControl.valueChanges
    - concat:
        + emit các giá trị của observable theo thứ tự truyền vào, xong observable này mới đến observable kia
- HOOs
    - switchMap:
        + unsubscribe Inner Observable khi có Outer Observable emit tiếp
        + Thường dùng trong query input để tránh lấy cả dữ liệu cũ không dùng đến nữa
    - mergeMap:
        + Vẫn subscribe Inner Observerble khi Outer Observable mới emit ~ giữ nhiều Subscription
        + Thường dùng nghiệp vụ liên quan đến write vào DB, download
        + Khi tham số concurrent = 1 thì mergeMap sẽ hoạt động như concatMap
    - concatMap:
        + Inner Observable complete thì mới subscribe vào Inner Observable tiếp theo
        + Thường dùng trong delete method
    - exhaustMap:
        + Khi Inner Observable cũ chưa complete mà có Inner Observable mới thì Inner Observable mới sẽ hoàn toàn bị bỏ qua
        + Mình đã dùng trong trường hợp login, register
    - switch/concat/mergeMapTo():
        + Thay vì truyền vào project function thì truyền vào Inner Observable luôn, không quan tâm đến giá trị mà Outer Observable emit ra
- UTILITY:
    - tap:
        + Log ra giá trị được emit từ Observable ở bất cứ thời điểm nào(trước, sau khi dùng 1 operator nào đó)
    - delay: 
        + khá giống setTimeout()
    - delayWhen:
        + Hoãn emit giá trị của Outer Observable đến khi Inner Observable emit
    - finalize:
        + Được thực thi khi 1 Observable complete hoặc error -> Thường dùng để stop load spinner
- FILTERING:
    - first:
    - last: 
    - take: 
    - takeUntil:
    - skip:
    - skipUntil:
    - debounceTime:
    - throttleTime:

- Overview:
    - Observables:
    - Observer:
    - Operators:
    - Subscription:
    - Subjects:
    