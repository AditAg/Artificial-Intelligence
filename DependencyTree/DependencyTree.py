#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<stack>
#include<bits/stdc++.h>
using namespace std;
typedef struct pcfgtreenode{
    string phrase;
    string head;
    vector<struct pcfgtreenode *> children;
}CFGNode;
typedef struct deptreenode{
    string word;
    string type;
    struct pcfgtreenode * C;
    vector<struct deptreenode *>children;

}dtnode;
map< string, vector<string> > rules;
void define_rules(){
    rules["ROOT"].push_back("S");
    rules["S"].push_back("VP");
    rules["NP"].push_back("NN");
    rules["NP"].push_back("NNS");
    rules["NP"].push_back("NNP");
    rules["NP"].push_back("NNPS");
    rules["NP"].push_back("PRP");
    rules["NP"].push_back("PRP$");
    rules["NP"].push_back("NP");
    rules["VP"].push_back("VBD");
    rules["VP"].push_back("VP");
    rules["VP"].push_back("VB");

    rules["VP"].push_back("VBG");
    rules["VP"].push_back("VBN");
    rules["VP"].push_back("VBP");
    rules["VP"].push_back("VBZ");
    rules["PP"].push_back("NP");
}
string determine_head(CFGNode *mainphrase){
    string phrasetosee = mainphrase->phrase;
    if(mainphrase->children.size()==1){
        return (mainphrase->children[0])->head;
    }
    else if(phrasetosee != "VP"){
        vector<string> rr = rules[phrasetosee];
        vector< struct pcfgtreenode* > ::iterator it;
        for(it=mainphrase->children.begin();it!=mainphrase->children.end();it++){
            if(find(rr.begin(),rr.end(),(*it)->phrase)!=rr.end()){
                return (*it)->head;
            }
        }
    }
    else{
        vector<string> rr = rules[phrasetosee];
        vector< pair<string,string> > heads;
        vector< struct pcfgtreenode* > ::iterator it;
        for(it=mainphrase->children.begin();it!=mainphrase->children.end();it++){
            if(find(rr.begin(),rr.end(),(*it)->phrase)!=rr.end()){
                if((*it)->phrase == "VP"){
                        return (*it)->head;
                }
                else{
                heads.push_back(make_pair((*it)->phrase,(*it)->head));
                }
            }
        }
        return heads[0].second;
    }
}
void print(dtnode*root, ofstream &file2)
{
    if((root->children).size()<=0){
        return;
    }
    file2 << root->word <<",";
    cout <<"("<< root->word<<" "<<root->type<<")"<< "->";
    for(int i=0;i<(root->children).size(); i++)
        {
            cout <<"(" <<root->children[i]->word <<" "<<root->children[i]->type<<")"<<",";
            file2 << root->children[i]->word << ",";
        }
    cout << endl;
    file2 <<"\n";
    for(int i=0;i<(root->children).size(); i++)
        print(root->children[i], file2);
}
void print2(CFGNode *root)
{
    cout << root->phrase<<","<<root->head << "->";
    for(int i=0;i<(root->children).size(); i++)
        {
            cout <<"("<<root->children[i]->phrase<<","<<root->children[i]->head<<")" << ",";
        }
    cout << endl;
    for(int i=0;i<(root->children).size(); i++)
        print2(root->children[i]);
}
int main()
{
    string line;
    vector<string> inputsentences;
    ifstream myfile ("input.txt");
    if(myfile.is_open()){
        while(getline(myfile,line)){
            inputsentences.push_back(line);
        }
        myfile.close();
    }
    else{
        cout<<"Sorry unable to open input file"<<endl;
        return 0;
    }
    define_rules();
    for(int i=0;i<inputsentences.size();i++)
    {
        stack<CFGNode *> pcfgtree;
        istringstream iss(inputsentences[i]);
        string sub;
        vector<string> subparts;
        while(iss>>sub){
            subparts.push_back(sub);
            int j;
            string s;
            if(sub[0]=='('){
                j=0;
                while(sub[j]=='('){
                    CFGNode * temp = new CFGNode;
                    temp->phrase=string(1,sub[j]);
                    pcfgtree.push(temp);
                    j++;
                }
                s = sub.substr(j);
                CFGNode * temp2 =new CFGNode;
                temp2->phrase=s;
                pcfgtree.push(temp2);
            }
            if(sub[sub.length()-1] == ')'){
                j=sub.length()-1;
                while(sub[j]==')'){
                    j--;
                }
                s=sub.substr(0,j+1);
                CFGNode * temp2 =new CFGNode;
                temp2->phrase=s;
                temp2->head=s;
                pcfgtree.push(temp2);
                int countbraces = sub.length()-(j+1);
                while(countbraces>0){
                    vector<CFGNode *> a;
                    while(pcfgtree.top()->phrase != "("){
                        CFGNode* temp = pcfgtree.top();
                        pcfgtree.pop();
                        a.push_back(temp);
                    }
                    CFGNode *mainphrase=a[a.size()-1];
                    a.pop_back();
                    while(a.size()!= 0){
                        mainphrase->children.push_back(a[a.size()-1]);
                        a.pop_back();
                    }
                    mainphrase->head= determine_head(mainphrase);
                    pcfgtree.pop();
                    pcfgtree.push(mainphrase);
                    countbraces--;
                }
            }

        }
        struct pcfgtreenode* root = pcfgtree.top();
        pcfgtree.pop();

        //Root stores head of PST.
        stack<dtnode *> dttree;
        dtnode* temp3 = new dtnode;
        temp3->word=root->head;
        temp3->type=root->phrase;
        temp3->C = root;
        dttree.push(temp3);
        struct pcfgtreenode* cval;
        int a;
        while(!dttree.empty()){
            dtnode *temp4 = dttree.top();
            dttree.pop();
            a=0;
            vector< struct pcfgtreenode* > ::iterator it;
            for(it=temp4->C->children.begin();it!=temp4->C->children.end();it++){
                if((*it)->head != temp4->word){
                    dtnode * temp5 = new dtnode;
                    temp5->word=(*it)->head;
                    temp5->C=(*it);
                    temp5->type = (*it)->phrase;
                    dttree.push(temp5);
                    temp4->children.push_back(temp5);
                }
                else{
                    cval=(*it);
                    a=1;
                }
            }
            if((a==1 && temp4->C->phrase =="ROOT") || (a==1 && temp4->C->children.size()>1 )){
                temp4->C= cval;
                dttree.push(temp4);
            }
        }
        print2(root);
        /*vector< dtnode* > ::iterator it;
        for(it=temp3->children.begin();it!=temp3->children.end();it++){
           cout<<(*it)->type<<" "<<(*it)->word<<endl;
        }*/
        //Temp3 stores head of Dependency Tree.
        //Do show individual relations among words by going through DT obtained above.

        ofstream file2;
        file2.open("output.txt");
        print(temp3, file2);
        file2.close();
        dtnode *root2 = temp3;
        string k1,k2;
        for(int i=0;i<(root2->children).size();i++){
            if(root2->children[i]->type == "NP" || root2->children[i]->type == "PP"){
                k1 = root2->children[i]->word;
                break;
            }
        }
        int z=0;
        //cout<<root2->children[0]->word<<" "<<root2->children[1]->word<<" "<<root2->children[2]->word<<endl;
        for(int i=0;i<(root2->children).size();i++){
            if((root2->children[i]->type == "NP" || root2->children[i]->type == "PP") && z==0){
                z+=1;
                continue;
            }
            else if(z==1 && root2->children[i]->type =="NP"){
                k2 = root2->children[i]->word;
                z+=1;
                break;
            }
        }
        cout<<"K1 "<< k1<<endl;
        cout<<"K2 "<< k2<<endl;
        for(int i=0;i<(root2->children).size();i++){
            if(root2->children[i]->type=="PP"){
                for(int j=0;j<(root2->children[i]->children).size();j++){
                    if(root2->children[i]->children[j]->word == "in" || root2->children[i]->children[j]->word == "on"){
                        cout<<"K7p "<< root2->children[i]->word<<endl;
                    }
                    else if(root2->children[i]->children[j]->word == "to" || root2->children[i]->children[j]->word == "for" ){
                        cout<<"K4 "<< root2->children[i]->word<<endl;
                    }
                    else if(root2->children[i]->children[j]->word == "from"){
                        cout<<"K5 "<< root2->children[i]->word<<endl;
                    }
                     else if(root2->children[i]->children[j]->word == "by"){
                        cout<<"K3 "<< root2->children[i]->word<<endl;
                    }
                    else if(root2->children[i]->children[j]->word == "at"){
                        cout<<"K7t "<< root2->children[i]->word<<endl;
                    }

                }
            }
        }
        //pri2(root);
        }

    return 0;

}
