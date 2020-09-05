const unitFieldUpdate = () => {
  const unit_select = document.getElementById("units");
  const unit_description_field = document.getElementById("description");

  var buf = "";
  var newouterHTML = "";

  unit_select.addEventListener("change", () => {
    unit_id = unit_select.value;
    console.log("unit_id: " + unit_id);
    console.log("outerHTML: " + unit_description_field.outerHTML);
    fetch("/kookboek/manage_units/unit_description/" + unit_id).then(function (
      response
    ) {
      response.json().then(function (data) {
        console.log("unit description: " + data.unit_description);
        buf = unit_description_field.outerHTML;
        console.log("buf=" + buf);
        newHTML =
          buf.slice(0, buf.indexOf("value=")) +
          'value="' +
          data.unit_description +
          '">';
        console.log("newHTML: " + newHTML);
        unit_description_field.outerHTML = newHTML;
        console.log("outerHTML: " + unit_description_field.outerHTML);
        console.log("innerHTML: " + unit_description_field.innerHTML);
      });
    });
  });
};

unitFieldUpdate();
