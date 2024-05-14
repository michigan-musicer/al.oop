package examples;

public interface Container<T> {
    public boolean empty();
    public int size();
    public T next();
    public void push(T elt);
    public T pop();
}
