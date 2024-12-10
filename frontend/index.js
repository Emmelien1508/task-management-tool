document.addEventListener("DOMContentLoaded", () => {
    new DocumentController()
})

class DocumentController {
    constructor() {
        this.initialData = null
        this.container = document.querySelector(".container")

        this.init()
    }

    async init() {
        const response = await fetch("http://localhost:8000")
        const data = await response.json()

        for (let task of data) {
            console.log("Task")

            const div = document.createElement("div")
            div.className = "task"

            const title = document.createElement("h2")
            title.innerText = task.title

            const description = document.createElement("p")
            description.innerText = task.description

            div.appendChild(title)
            div.appendChild(description)

            this.container.appendChild(div)
        }
    }
}