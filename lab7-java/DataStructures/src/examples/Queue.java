package examples;

import java.util.ArrayList;

public class Queue<T> implements Container<T> {
    private ArrayList<T> _container;
    public Queue()
    {
        this._container = new ArrayList<>();
    }

    @Override
    public boolean empty()
    {
        return this._container.isEmpty();
    }

    @Override
    public int size()
    {
        return this._container.size();
    }
    @Override
    public T next() {
        return this._container.getFirst();
    }

    @Override
    public void push(T elt) {
        this._container.add(elt);
    }

    @Override
    public T pop() {
        return this._container.removeFirst();
    }
}
