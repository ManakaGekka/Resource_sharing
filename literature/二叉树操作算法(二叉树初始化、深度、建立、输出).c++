#include<iostream.h>
#include<STRSTREAM.H>
typedef char elemtype;
struct btreenode
{
    elemtype data;
    btreenode *lchild;
    btreenode *rchild;
};
void initbtree ( btreenode *&bt )
{ bt=NULL;}
 
void precrttree ( btreenode *&bt )
{
    char ch;
    cin>>ch;
    if ( ch=='#' )
        bt=NULL;
    else
    {
        bt=new btreenode;
        bt->data=ch;
        precrttree ( bt->lchild );
        precrttree ( bt->rchild );
    }
}
 
void crtbtree ( btreenode *&bt,char *a )
{
    char ch;
    btreenode *s[20];
    int top=-1;
    bt=NULL;
    btreenode *p;
    int k;
    istrstream ins ( a );
    ins>>ch;
    while ( ch!='@' )
    {
        switch ( ch )
        {
        case'(':
            top++;
            s[top]=p;
            k=1;
            break;
        case')':
            top--;
            break;
        case',':
            k=2;
            break;
        default:
            p=new btreenode;
            p->data=ch;
            p->lchild=p->rchild=NULL;
            if ( bt==NULL )
                bt=p;
            else
            {
                if ( k==1 )  s[top]->lchild=p;
                else s[top]->rchild=p;
            }
        }
        ins>>ch;
    }
}
 
int btreeempty ( btreenode *bt )
{ return bt==NULL;}
 
void preorder ( btreenode *bt )
{
    if ( bt!=NULL )
    {
        cout<<bt->data<<' ';
        preorder ( bt->lchild );
        preorder ( bt->rchild );
    }
}
 
void inorder ( btreenode *bt )
{
    if ( bt!=NULL )
    {
        inorder ( bt->lchild );
        cout<<bt->data<<' ';
        inorder ( bt->rchild );
    }
}
 
void postorder ( btreenode *bt )
{
    if ( bt!=NULL )
    {
        postorder ( bt->lchild );
        postorder ( bt->rchild );
        cout<<bt->data<<' ';
    }
}
 
void levorder ( btreenode *bt )
{
    btreenode *q[30];
    int front=0,rear=0;
    btreenode *p;
    if ( bt!=NULL )
    {
        rear= ( rear+1 ) %30;
        q[rear]=bt;
    }
    while ( front!=rear )
    {
        front= ( front+1 ) %30;
        p=q[front];
        cout<<p->data<<' ';
        if ( p->lchild!=NULL )
        {
            rear= ( rear+1 ) %30;
            q[rear]=p->lchild;
        }
        if ( p->rchild!=NULL )
        {
            rear= ( rear+1 ) %30;
            q[rear]=p->rchild;
        }
    }
}
 
int btreedepth ( btreenode *bt )
{
    if ( bt==NULL )
        return 0;
    else
    {
        int dep1=btreedepth ( bt->lchild );
        int dep2=btreedepth ( bt->rchild );
        if ( dep1>dep2 )
            return dep1+1;
        else
            return dep2+1;
    }
}
 
int btreecount ( btreenode *bt )
{
    if ( bt==NULL )
        return 0;
    else
        return btreecount ( bt->lchild ) +btreecount ( bt->rchild ) +1;
 
}
 
int btreeleafcount ( btreenode *bt )
{
    if ( bt==NULL )
        return 0;
    else if ( bt->lchild==NULL&&bt->rchild==NULL )
        return 1;
    else return btreeleafcount ( bt->lchild ) +btreeleafcount ( bt->rchild );
}
 
void printbtree ( btreenode *bt )
{
    if ( bt==NULL )
        return;
    else
    {
        cout<<bt->data;
        if ( bt->lchild!=NULL||bt->rchild!=NULL )
        {
            cout<<'(';
            printbtree ( bt->lchild );
            if ( bt->rchild!=NULL )
                cout<<',';
            printbtree ( bt->rchild );
            cout<<')';
        }
    }
}
 
void clearbtree ( btreenode *&bt )
{
    if ( bt!=NULL )
    {
        clearbtree ( bt->lchild );
        clearbtree ( bt->rchild );
        delete bt;
        bt=NULL;
    }
}
 
void main()
{
    btreenode *bt;
    initbtree ( bt );
    char b[50];
    int tag;
    cout<<"1.pre order create btree"<<endl;
    cout<<"2.glist create btree"<<endl;
    cout<<"input selecte 1 or 2:";
    cin>>tag;
    if ( tag==2 )
    {
        cout<<"input @ end glist:"<<endl;
        cin.getline ( b,sizeof ( b ) );
        crtbtree ( bt,b );
    }
    else
    {
        cout<<"input pretree and '#':"<<endl;
        precrttree ( bt );
    }
    printbtree ( bt );
    cout<<endl;
    cout<<"pre order:";
    preorder ( bt );
    cout<<endl;
    cout<<"in order:";
    inorder ( bt );
    cout<<endl;
    cout<<"post order:";
    postorder ( bt );
    cout<<endl;
    cout<<"level order:";
    levorder ( bt );
    cout<<endl;
    cout<<"btree depth is:";
    cout<<btreedepth ( bt ) <<endl;
    cout<<"btree node num is:";
    cout<<btreecount ( bt ) <<endl;
    cout<<"btree leaf node num is:";
    cout<<btreeleafcount ( bt ) <<endl;
    clearbtree ( bt );
}
