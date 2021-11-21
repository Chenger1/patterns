abstract class Component{
    protected parent: Component;

    public addParent(component: Component){
        this.parent = component;
    }
    
    public getParent(){
        return this.parent;
    }

    public abstract makeJob():string;
}


class Leaf extends Component{
    public makeJob(){
        return 'Leaf';
    }
}


class Composite extends Component{
    protected children: Component[] = [];

    public addChildren(component: Component){
        this.children.push(component);
        component.addParent(this);
    }

    public removeChildren(component: Component){
        const componentPlace = this.children.indexOf(component);
        this.children.splice(componentPlace, 1);
    }

    public makeJob(){
        const result = [];
        for(let child of this.children){
            result.push(child.makeJob())
        }
        return result.join('-');
    }
}

function clientCode(){
    const tree = new Composite();
    const branch1 = new Composite();
    branch1.addChildren(new Leaf());
    branch1.addChildren(new Leaf());
    tree.addChildren(branch1);
    console.log(tree.makeJob());
}

clientCode();
