- JPA Cascade Type:
    - Sử dụng cascade type trong các trường hợp tham chiếu ít, các dữ liệu tham chiếu chỉ có ý nghĩa khi gắn liền với đối tượng tham chiếu
    - type:
        - PERSIST (lưu 1 object mới)
        - MERGE (cập nhật 1 object)
        - REMOVE (xóa 1 object)
        - REFRESH
        - DETACH
- Mapping:
    - [One-To-One]
    - [@ManyToOne]:
        - [@JoinColumn]: 
            - chỉ định property thuộc bảng hiện tại sẽ ánh xạ tới PK của bảng được tham chiếu tới.
    - [@OneToMany]:
        - [mappedBy]:
            - chỉ định tên của property được định nghĩa với @ManyToOne trong table chứa FK
    - [@ManyToMany]:
        - [@JoinTable](name = ..., joinColumns = ..., inverseJoinColumns = ...)
            - name: tên bảng join
            - joinColumns: tên column trong join table mà bảng khai báo sẽ FK tới
            - inverseJoinColumns: tên colum trong join table mà bảng còn lại FK tới
- Hibernate ORM: 
    - là 1 ORM tool cho Java
    - JPA là vũ đạo, Hibernate là vũ công
    - JPA là interface, Hibernate là implementation
- @Entity:
    - POJO vs JavaBean
        - POJO: plain old java object
            - 1 POJO không extends 1 class, không implements 1 interface, không chứa annotations
        - JavaBean: 
            - là 1 kiểu đặc biệt của POJO
            - tất cả properties phải là private, phải có getter hoặc setter hoặc cả 2
            - phải có 1 no-arg constructor
    - @Entity: để biến 1 JavaBean trở thành 1 entity để chúng có thể thao tác vói DB khi sử dụng DB này
    - @Table: sử dụng khi muốn thay đổi tên bảng của DB mà không muốn thay đổi tên Entity

# REF
PK: primary key
FK: foreign key
