import java.util.ArrayList;

public class VectorSolution<T> {
    private ArrayList<T> _container;
    public VectorSolution()
    {
        this._container = new ArrayList<>();
    }

    public boolean empty()
    {
        return this._container.isEmpty();
    }

    public int size()
    {
        return this._container.size();
    }

    public T get(int index)
    {
        return this._container.get(index);
    }

    public void pushBack(T elt)
    {
        this._container.addLast(elt);
    }

    public void pushFront(T elt)
    {
        this._container.addFirst(elt);
    }

    public T popBack()
    {
        return this._container.removeLast();
    }

    public T popFront()
    {
        return this._container.removeFirst();
    }

}
