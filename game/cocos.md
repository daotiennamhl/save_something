- Thao tác với 1 component:
    - Thêm properties
    - Lifecycle callback
    - Lấy thông tin của 1 component bất kì:
        - Lấy thông tin của component con, cha
        - update node transform: Node con ảnh hưởng bởi các thông số của node cha
- Lifecycle callback:
    - onLoad: initialization phase of the component script
    - start: call before first update, usually used to initialize data that needs frequent modification
    - update
    - lateUpdate: call after update of all components are done
    - onDestroy: when component or node call destroy(), it will call the onDestroy callback
    - onEnable: after onLoad and before start if the node is created for the first time. Else when the enabled property of the component turns from false to true
    - onDisable: Ngược lại với enable là disable
    - onLoad -> onEnable -> start -> update -> lastUpdate -> onDisable -> onDestroys
- Chuyển screen