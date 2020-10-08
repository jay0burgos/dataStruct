import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { Villian} from '../villian'

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {

  hero: Hero = {
    id: 1,
    name: 'Windstorm'
  }
  villan: Villian = {
    id:1,
    name: 'Wrecker'
  }

  constructor() { }

  ngOnInit(): void {
  }

}



/*
Notes-
<h2>{{hero.name | uppercase}} Details</h2>
                ^pipe operator followed by a pipe which is used to format 
                strings, currency amounts, dates and other display data
                https://angular.io/guide/pipes
*/