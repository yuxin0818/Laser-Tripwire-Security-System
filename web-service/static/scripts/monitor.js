
// all devices' names.
var device_ids = [];
// mapping between device id and device info.
let device_info = new Map();

$(document).ready(function() {
    console.log("Load Sucessfully...");
    setInterval(function() {
        $.get('/api/v1/request/get_id', function(data) {
            device_ids = data.devices;
            update_dashboard_headers(data.devices);
        });

        $.get('/api/v1/request/get_id', function(data){
            let devices = data.devices
            for(var i = 0; i < devices.length; i++) {
                let cur_id = devices[i];
                my_map_id.set(i, devices[i])
                $.get('/api/v1/request/get_each_info', {device_id: cur_id}, function(device_info) {
                    let cur_info = device_info;
                    my_map_full.set(cur_id, cur_info);
                });
            }
        });

        let first_id = my_map_id.get(1);
        $("#Device-1").text(my_map_id.get(1));
        $("#Status-1").text(my_map_full.get(first_id))

    }, 1000)
});

var update_dashboard_headers = function(devices) {
    for (var i = 0 ; i < devices.length ; i++) {
        let index = i + 1;
        let html_card_header_id = "#device-header-" + index;
        $(html_card_header_id).text(devices[i]);
        let html_card_id = "#device-card-" + index;
        $(html_card_header_id).addClass("bg-success");
    }
}

var update_device_display = function(device_id, device_info) {

}