import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import TreeView from '@material-ui/lab/TreeView';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';
import AddIcon from '@material-ui/icons/Add';
import TreeItem from '@material-ui/lab/TreeItem';
import IconButton from '@material-ui/core/IconButton';
import TextField from '@material-ui/core/TextField';


const useStyles = makeStyles({
  root: {
    height: 216,
    flexGrow: 1,
    maxWidth: 400,
  },
});

export interface GroupedWords {
  [key: string]: string[]
};

export default function FolderView() {
  const classes = useStyles();
  const [expanded, setExpanded] = React.useState<string[]>([]);
  const [selected, setSelected] = React.useState<string[]>([]);
  const [groupedWords, setGroupedWords] = React.useState<GroupedWords>({});
  const [hovering, setHovering] = React.useState<boolean>(false);
  const [editable, setEditable] =  React.useState<boolean>(false);
  const [updatedText, setUpdatedText] = React.useState<string>('');

  useEffect(() => {
    fetch('/groupedWords/').then(res => res.json()).then(data => {
      setGroupedWords(data);
    });
  }, []);

  const handleToggle = (event: React.ChangeEvent<{}>, nodeIds: string[]) => {
    setExpanded(nodeIds);
  };

  const handleSelect = (event: React.ChangeEvent<{}>, nodeIds: string[]) => {
    setSelected(nodeIds);
  };

  const handleMouseOver = () => {
    console.log('is hover',hovering)
    setHovering(!hovering);
  }

  const handleAddWord = () => {
    setEditable(true);
  }

  const handleSaveWord = () => {
    setEditable(false);
    setUpdatedText('');
    const requestOptions = {
      method: 'POST'
    };
    fetch('/addWord/' + updatedText, requestOptions)
      .then(res => res.json())
      .then(data => {
        setGroupedWords(data);
      });
  }
  

  const handleWordChange = (e: any) => {
    setUpdatedText(e.target.value);
  }
  return (
    <TreeView
      className={classes.root}
      defaultCollapseIcon={<ExpandMoreIcon />}
      defaultExpandIcon={<ChevronRightIcon />}
      expanded={expanded}
      selected={selected}
      onNodeToggle={handleToggle}
      onNodeSelect={handleSelect}
    >
      {
        Object.keys(groupedWords).map((key) => {
          return <TreeItem nodeId={key.toString()} label={<div>{key}<IconButton onClick={handleAddWord}><AddIcon/></IconButton></div>} 
          onMouseEnter={handleMouseOver} onMouseLeave={handleMouseOver} 
       >
            {editable?
              <form className={classes.root} noValidate autoComplete="off">
                <TextField id="filled-basic" label="Filled" variant="filled" value={updatedText} onChange={handleWordChange} onBlur={handleSaveWord}/>
              </form>:<div/>
            } 
            {
              groupedWords[key].map((keyword: string, index: number) => {
                return <TreeItem nodeId={index.toString()} label={keyword}/>
              })
            }
          </TreeItem>
        })
      }
    </TreeView> 
  );
}
//<IconButton onClick={handleAddWord}>