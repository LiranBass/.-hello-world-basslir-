console.log("first_try");

fetch('https://reqres.in/api/users?page=2').then(Response => Response.json())
.then(responseJSON => createUsersList(responseJSON.data)).catch(err =>
console.log(err));

function createUsersList(users){
    console.log(users);
    const curr_main=document.querySelector("main");
    for (let user of users){
        const section=document.createElement("section");
        section.innerHTML= `
        ${user.first_name}
        
        `;
        curr_main.appendChild(section);
    }
}