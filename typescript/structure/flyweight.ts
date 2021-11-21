class Format{
    public name: string;

    constructor(name: string){
        this.name = name;
    }
}

class Book{
    public title: string;
    public format: Format;

    constructor(title: string, format: Format){
        this.title = title;
        this.format = format;
    }
}

class BookFormatFactory{
    private formats: {[key: string]: Format} = <any>{};

    public getFormat(format_name: string){
        if(!(format_name in this.formats)){
            this.formats[format_name] = new Format(format_name);
        }
        return this.formats[format_name];
    }
}


const formats = ['pdf', 'epub', 'fb2', 'docx', 'txt'];

function clideCode(){
    const books = [];
    const bookFactory = new BookFormatFactory();
    for(let i = 0 ; i <= 1000; i++){
        let form = formats[Math.floor(Math.random()*formats.length)];
        let form_obj = bookFactory.getFormat(form);
        books.push(new Book(`Book with ${i}`, form_obj)); 
    }

    console.log(books.map((item) => `Book ${item.title} with format: ${item.format.name}\n`).join(':'));
}
clideCode();
