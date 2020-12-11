
// all devices' names.
var devices = [];
// mapping between device id and device info.
let devices_info = {};
// number of milliseconds needed to determine if a device is offline since last ping.
let connection_lost_threashold = 5000;

$(document).ready(function() {
    console.log("Load Sucessfully...");
    setInterval(function() {
        $.get('/api/v1/devices', function(data) {
            device_ids = data.devices;
            update_device_list(device_ids);
        });

        for (let i = 0 ; i < devices.length ; i++) {
            url = '/api/v1/device/' + devices[i];
            $.get(url, function(data) {
                let device_info = data.device_info;
                update_device_info_data(i, device_info)
            })
        }
    }, 500)

    setInterval(update_view, 500);
});

var update_device_list = function(device_list) {
    devices = device_list;
}

var update_device_info_data = function(device_index, device_info) {
    devices_info[device_index] = device_info;
}

var update_view = function() {
    for (let i = 0 ; i < devices.length ; i++) {
        let device_name = devices[i];
        let device_info = devices_info[i];
        if (device_info === undefined) {
            continue;
        }
        let index = i + 1;
        let html_card_header_id = "#device-header-" + index;
        let html_card_footer_id = "#device-last-update-text-" + index;
        let html_card_id = "#device-card-" + index;
        let status_id = "#status-" + index;
        let reset_button_id = "#reset-button-" + index;
        $(html_card_header_id).text(devices[i]);
        let last_updated_time = new Date(0);
        last_updated_time.setUTCSeconds(device_info.last_ping_time);
        if (last_updated_time.getTime() == 0) {
            $(html_card_footer_id).text("never updated...");
        } else {
            // If it's invaded, then we don't refresh the UI until it's reset.
            if (isInvaded(i)) {
                $(status_id).text("Room Invaded!");
                $(reset_button_id).removeClass("invisible");
                $(reset_button_id).unbind('click');
                $(reset_button_id).on('click', function(event) {
                    event.preventDefault();
                    $.ajax({
                        url: '/api/v1/device/reset',
                        type: 'POST',
                        data: JSON.stringify({
                            'device_id': device_name,
                        }),
                        contentType:"application/json",
                        dataType:"json",
                        success: function(data){
                            if (data.status == "OK") {
                                console.log("Reset succeeded.");
                            } else {
                                console.log("Reset failed.");
                            }
                        }
                    });
                });
                $(html_card_footer_id).text(`Room invaded at ${getLastInvadeTimeForDevice(i).toLocaleTimeString()}`);
                setBgColor(html_card_id, "#800000");
                continue;
            }
            $(reset_button_id).addClass("invisible");
            let cur_time = new Date();
            let time_since_last_ping = cur_time.getTime() - last_updated_time.getTime();
            if (time_since_last_ping > connection_lost_threashold) {
                let time_out_seconds = Math.floor(time_since_last_ping / 1000);
                $(html_card_footer_id).text(last_updated_time.toLocaleTimeString() + ` (No ping for ${time_out_seconds} secs)`);
                $(status_id).text("Timed out!");
                console.log(`Connection to ${device_name} is lost... Warning threshold ${connection_lost_threashold} ms. Actual time passed since last ping ${time_since_last_ping} ms.`);
                setBgColor(html_card_id, "#daa520");
            } else {
                $(status_id).text("Operating Normally");
                $(html_card_footer_id).text(last_updated_time.toLocaleTimeString());
                setBgColor(html_card_id, "#4169E1");
            }
        }
    }
}

var setTextColor = function(id, text_color) {
    $(id).css("color", text_color);
}

var setBgColor = function(id, bg_color) {
    $(id).removeClass("bg-secondary");
    $(id).css("background-color", bg_color);
}

var isInvaded = function(device_index) {
    let device_info = devices_info[device_index];
    let reset_time = new Date(0);
    reset_time.setUTCSeconds(device_info.reset_time);
    let last_incident_time = new Date(0);
    last_incident_time.setUTCSeconds(device_info.last_incident_time);
    if (last_incident_time.getTime() > reset_time.getTime()) {
        return true;
    }
    return false;
}

var getLastInvadeTimeForDevice = function(device_index) {
    time = new Date(0);
    time.setUTCSeconds(devices_info[device_index].last_incident_time);
    return time;
}
