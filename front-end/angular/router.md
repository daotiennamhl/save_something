- basic:
    + thêm router cho dự án mới thì --routing
    + RouterModule.forRoot() vs forChild()
    + Router service: 
        + navigate route
        + observe router event
    + ActivatedRoute: paramMap(slug), queryParamMap
- lazyload: 
    + import('...') syntax cho angular 8 trở lên, còn trước đó sẽ dùng magic string
    + có thể preload all module cũng có thể config vài module thôi
- Angular Router Navigation Cycle:
    + router guards: dùng canActive() để check xem có được active các components hay không
    + dùng canDeactive() để check xem có được deactive 1 component hay không(ví dụ: hỏi trước người dùng khi muốn rời trang hiện tại)
    + resolver có thể dùng để lấy trước 1 phần data cho component trước khi render component -> indicator loading sẽ không loading khi lấy phần data đó
