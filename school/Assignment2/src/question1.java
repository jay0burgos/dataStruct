public class question1 {
    public class dualStackArray<arrayType>{ //generic to allow multi variable use
        //gonna need push, pop, and top methods
        private arrayType[] arr;
        private int top1;
        private int top2;
        private int midPoint;

        public dualStackArray(int size) {
            this.arr = (arrayType[]) new Object[size];
            this.top1 = -1;
            this.top2 = arr.length;

        }
        public void push(int stack, arrayType newObject){
              switch (stack){    //chooses which stack to push
                  case 1:
                  {
                      if (!(top1+1 == top2))
                      {
                           arr[top1+1] = newObject;
                           this.top1++;
                      }
                      else
                          System.out.println("Overflow error");
                  }
                  case 2:
                  {
                      if (!(top2-1 == top1))
                      {
                          arr[top2-1] = newObject;
                          this.top2--;
                      }
                      else
                          System.out.println("Overflow error");
                  }
              }
        }
        public arrayType pop(int stack){
            switch (stack){    //chooses which stack to pop
                case 1:
                {
                    if (!(top1 == -1)) //checks if its empty
                    {
                        this.top1--;
                        return arr[top1+1];
                    }
                    else
                        System.out.println("Stack is empty");
                }
                case 2:
                {
                    if (!(top2 == this.arr.length))//checks if its empty)
                    {
                        this.top2++;
                        return arr[top2-1];

                    }
                    else
                        System.out.println("Overflow error");
                }
                default:
                    return null;
            }
        }
    }
}
