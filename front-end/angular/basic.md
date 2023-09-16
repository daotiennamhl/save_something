- Decorator trong angular: 
    + Class decorator: @Component, @NgModule
    + Property Decorator: @Input, @Output, @Override
    + Method Decorator: @HostListener
    + Parameter Decorator: @Inject, @Self, @Optional, @SkipSelf

    + @Self: dùng ở constructor để lấy ra service của chính class đó chứ không phải lấy của parent class hoặc lấy từ module
    + @SkipSelf: Dùng ở constructor để bỏ qua service được khai báo ở class đó và lấy của parent class hoặc lấy từ module (ngược với @Self)
    