Blockly.Python['get_device'] = function(block) {
  // Search the text for a substring.
  var deviceInfo = JSON.parse(block.getFieldValue('DEVICE'))
  var client = 'M2XClient(key="06747f1fc8b034d194b298a803397e27").device("' + deviceInfo.id + '")'
  return [client, Blockly.Python.ORDER_MEMBER];
};


Blockly.Python['send_text'] = function(block) {
  // Search the text for a substring.
  var phoneNumber = Blockly.Python.valueToCode(block, 'PHONE_NUMBER', Blockly.Python.ORDER_ADDITION)
  var phoneMessage = Blockly.Python.valueToCode(block, 'PHONE_MESSAGE', Blockly.Python.ORDER_ADDITION)
  var code = 'client.messages.create(to="+" +' + phoneNumber + ', from_="+18082010713", body=' + phoneMessage + ')'
  return code;
}

Blockly.Python['last_record'] = function(block) {
  var code = 'float(' + Blockly.Python.valueToCode(block, 'DEVICE', Blockly.Python.ORDER_ADDITION) + '.streams()[0].values()["values"][-1]["value"])'
  return [code, Blockly.Python.ORDER_MEMBER]
}


function guid() {
  function s4() {
    return Math.floor((1 + Math.random()) * 0x10000)
      .toString(16)
      .substring(1);
  }
  return s4() + s4() + s4();
}

function newVariable(content) {
   return guid() + ' = ' + content
}
