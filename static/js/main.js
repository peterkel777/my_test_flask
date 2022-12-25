function btn_act(input_id) {
    //alert(input_id);
    //var checked_input = document.getElementById(input_id);
    var checked_input = document.querySelector("input[id=" + input_id + "]")
    var checked_label = document.querySelector("label[name=" + input_id + "]")
    var remove_btn = document.getElementById("remove_btn");

    if (checked_input.checked) {
        checked_label.style.textDecoration = "line-through";        
        }
    else {
        checked_label.style.textDecoration = "";
    }

    remove_btn.style.backgroundColor = "#FE7575";
    remove_btn.style.cursor = "pointer";
}