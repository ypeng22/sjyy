

let addUser = function (name, match_t, bio){
    let output = 'user { \n\t\'name\': \'' + name + '\'\n\t\'match_t\': \'' + match_t + '\'\n\t\'bio\': \'' + bio + '\'\n}'
    alert(output)
}

let queryDB = function (args) {
}

module.exports = {
    addUser,
    queryDB
}