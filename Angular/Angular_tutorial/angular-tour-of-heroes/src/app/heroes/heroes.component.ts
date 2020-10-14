import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { Villian } from '../villian'
import {HEROES} from '../mock-heroes'


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
  villan: Villian = { //creates an object that uses the villan interface
    id:1,
    name: 'Wrecker',
    sayIntro: ()=>{return "You will never stop me"}
  }
  heroes = HEROES; //component property

  selectedHero: Hero;

  onSelect(hero: Hero): void {
    this.selectedHero = hero;
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