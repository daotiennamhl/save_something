- Decorator trong angular: 
    + Class decorator: @Component, @NgModule
    + Property Decorator: @Input, @Output, @Override
    + Method Decorator: @HostListener
    + Parameter Decorator: @Inject, @Self, @Optional, @SkipSelf

    + @Self: dùng ở constructor để lấy ra service của chính class đó chứ không phải lấy của parent class hoặc lấy từ module
    + @SkipSelf: Dùng ở constructor để bỏ qua service được khai báo ở class đó và lấy của parent class hoặc lấy từ module (ngược với @Self)
    
- Dependency Injection:
    + Injectable() show that class can be injected
    + providedIn: 'root' se tao ra mot single shared instance cho toan bo du an, neu khong providers o module hoac class thi moi khi module hoac class tao new instance service do cung se tao them 1 instance moi
    + Inject a dependency: 
      + Declare in a class constructor or use inject() method

- Change detection:
    + Use detectChanges() when you've updated the model after angular has run it's change detection, or if the update hasn't been in angular world at all.
    + Use markForCheck() if you're using OnPush and you're bypassing the ChangeDetectionStrategy by mutating some data or you've updated the model inside a setTimeout;